import Ember from 'ember';

export default Ember.Controller.extend({
  actions: {
    createKnot() {
      var knot = this.get('model'); // -> klappt beim speichern nicht
      var self = this;
      knot.save().then(function() {
        self.transitionToRoute('knots');
      }).catch(function(reason) {
      });
    },
  }
});
