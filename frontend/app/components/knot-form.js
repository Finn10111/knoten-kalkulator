import Ember from 'ember';
import { task } from 'ember-concurrency';

const { get, set } = Ember;

export default Ember.Component.extend({
  model() {
    return this.store.createRecord('knot');
  },
  store: Ember.inject.service(),

  uploadImage: task(function * (file) {
    let image = this.get('store').createRecord('image', {
      filename: get(file, 'name'),
      filesize: get(file, 'size')
    });

    try {
      file.readAsDataURL().then(function (url) {
        if (get(image, 'url') == null) {
          set(image, 'url', url);
        }
      });

      let response = yield file.upload('/api/images/upload');
	  console.log(response);
      set(image, 'name', response.body.filename);
	  var model = this.get('model');
	  model.set('image', response.body.filename)
      //yield image.save();
    } catch (e) {
	  console.log('upload error');
	  console.log(e);
      //image.rollback();
    }
  }).maxConcurrency(3).enqueue(),
  actions: {
    addCord() {
        let knot = this.get('model');
		let store = this.get('store');
        knot.get('cords').pushObject(store.createRecord('cord'));
    },
    uploadImage(file) {
      get(this, 'uploadImage').perform(file);
    }
  }
});
