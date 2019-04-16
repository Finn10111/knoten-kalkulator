import Controller from '@ember/controller';

export default Controller.extend({
  model() {
    return this.store.createRecord('knot');
  },
  actions: {
    deleteKnot() {
      var knot = this.get('model');
      var self = this;
      knot.destroyRecord().then(function() {
        self.transitionToRoute('knots');
      }).catch(function(reason) {
        alert(reason);
      });
    }
  }
});
