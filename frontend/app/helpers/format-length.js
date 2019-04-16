import { helper as buildHelper } from '@ember/component/helper';

export function formatLength(params/*, hash*/) {
  if ( params >= 100 ) {
    return (params / 100).toFixed(2) + ' m';
  } else {
    return parseFloat(params).toFixed(1) + ' cm';
  }
}

export default buildHelper(formatLength);
