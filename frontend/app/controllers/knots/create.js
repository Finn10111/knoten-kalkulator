import Ember from 'ember';

export default Ember.Controller.extend({
  model() {
    return this.store.createRecord('knot');
  },
  actions: {
    createKnot() {
      console.log("createKnot");
      var knot = this.get('model');
      var self = this;
      knot.save().then(function() {
        console.log("knoten gespeichert");
        self.transitionToRoute('knots');
      }).catch(function(reason) {
        console.log("fehler beim knoten speichern");
      });
    },
  }
});
