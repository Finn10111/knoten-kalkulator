import DS from 'ember-data';

export default DS.Model.extend({
    name: DS.attr('string'),
    image: DS.attr('string'),
    width: DS.attr('number'),
    thickness: DS.attr('number'),
    length: DS.attr('number'),
    cords: DS.hasMany('cord'),
});
