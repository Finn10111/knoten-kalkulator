import DS from 'ember-data';

export default DS.Model.extend({
    name: DS.attr('string'),
    image: DS.attr('string'),
    width: DS.attr('number'),
    thickness: DS.attr('number'),
    length: DS.attr('number'),
    cords: DS.hasMany('cord'),
		isRound: DS.attr('boolean'),
    extraLength: Ember.computed('isRound', 'thickness', function() {
      var extraLength = 0;
      if ( this.get('isRound') ) {
        extraLength = Math.PI * (parseInt(this.get('thickness')) / 10.0);
      }
      return extraLength;
    }),
    realNeededLength: Ember.computed('length', 'extraLength', function() {
      return parseFloat(this.get('length')) + this.get('extraLength');
    }),
});
