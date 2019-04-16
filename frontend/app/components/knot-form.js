import { task } from 'ember-concurrency';
import Component from '@ember/component';
import { inject } from '@ember/service';
import { get } from '@ember/object';
import { set } from '@ember/object';

export default Component.extend({
  model() {
    return this.store.createRecord('knot');
  },
  store: inject(),

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
      set(image, 'name', response.body.filename);
      var model = this.get('model');
      model.set('image', response.body.filename)
        //yield image.save();
    } catch (e) {
        //image.rollback();
    }
  }).maxConcurrency(3).enqueue(),
  actions: {
    addCord() {
      let knot = this.get('model');
      if ( !knot.get('cords') ) {
        knot.set('cords', []);
      }
      let store = this.get('store');
      knot.get('cords').pushObject(store.createRecord('cord'));
    },
    uploadImage(file) {
      get(this, 'uploadImage').perform(file);
    },
    removeCord(cord) {
      cord.deleteRecord();
    }
  }
});
