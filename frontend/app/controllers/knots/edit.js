import Ember from 'ember';

export default Ember.Controller.extend({
  model() {
    return this.store.createRecord('knot');
  },
  store: Ember.inject.service(),

  actions: {
    updateKnot() {
      var knot = this.get('model');
      var self = this;
      knot.save().then(function() {
        console.log("updateKnot");
		self.transitionToRoute('knots');
      }).catch(function(reason) {
      });
    },
  }
});
