import Component from '@ember/component';
import { computed } from '@ember/object';

export default Component.extend({
  isVisible: computed('cord.result', function() {
    return this.get('cord.result') > 0;
  }),
});
