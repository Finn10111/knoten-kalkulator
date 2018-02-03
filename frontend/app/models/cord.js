import DS from 'ember-data';

export default DS.Model.extend({
  knot: DS.belongsTo('knot'),
  name: DS.attr('string'),
  factor: DS.attr('number'),
  quantity: DS.attr('number'),
  result: DS.attr(),
});
