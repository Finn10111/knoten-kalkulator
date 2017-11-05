import Ember from 'ember';

export function formatLength(params/*, hash*/) {
  if ( params >= 100 ) {
      return (params / 100).toFixed(2) + ' m';
  } else {
      return Math.floor(params) + ' cm';
  }
}

export default Ember.Helper.helper(formatLength);
