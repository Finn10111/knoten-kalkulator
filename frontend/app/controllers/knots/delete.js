import Ember from 'ember';

export default Ember.Controller.extend({
  model() {
    return this.store.createRecord('knot');
  },
  actions: {
    deleteKnot() {
      console.log("deleteKnot()");
      var knot = this.get('model');
      var self = this;
      knot.destroyRecord().then(function() {
        console.log("jo");
        self.transitionToRoute('knots');
      }).catch(function(reason) {
        console.log("ne");
      });
    }
  }
});
