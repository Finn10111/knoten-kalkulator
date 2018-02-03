import Ember from 'ember';

export default Ember.Controller.extend({
  actions: {
    calcLength() {
      var model = this.get('model');
      var cords = model.get('cords');
      cords.forEach(function(cord) {
        var factor = cord.get('factor');
        var neededLength = factor * model.get('realNeededLength');
        cord.set('result', neededLength);
      });
    },
    toggleIsRound(value) {
      this.set('model.isRound', value);
      this.send('calcLength');
    }
  }
});
