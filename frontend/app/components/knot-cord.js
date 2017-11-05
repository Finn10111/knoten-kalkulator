import Ember from 'ember';

export default Ember.Component.extend({
    isVisible: Ember.computed('cord.result', function() {
        return this.get('cord.result') > 0;
    }),
});
