import Controller from '@ember/controller';

export default Controller.extend({
  model() {
    return this.store.createRecord('knot');
  },

  actions: {
    updateKnot() {
      var knot = this.get('model');
      var self = this;
      knot.save().then(function() {
        self.transitionToRoute('knots');
      }).catch(function(reason) {
        alert(reason);
      });
    },
  }
});
