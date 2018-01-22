import Ember from 'ember';

export default Ember.Controller.extend({
  actions: {
    createKnot() {
      var knot = this.get('model'); // -> klappt beim speichern nicht
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
