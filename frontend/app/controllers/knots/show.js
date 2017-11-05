import Ember from 'ember';

export default Ember.Controller.extend({
  actions: {
    calcLength() {
        console.log("calcLength");
        var model = this.get('model');
        var cords = model.get('cords');
        cords.forEach(function(cord) {
            var factor = cord.get('factor');
            var neededLength = factor * model.get('length');
            cord.set('result', neededLength);
        });
    }
  }
});
