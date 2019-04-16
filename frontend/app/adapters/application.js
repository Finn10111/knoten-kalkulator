import DS from 'ember-data';
import DataAdapterMixin from 'ember-simple-auth/mixins/data-adapter-mixin';

let headers = {'Accept': 'application/json'};

export default DS.RESTAdapter.extend(DataAdapterMixin, {
  authorizer: 'authorizer:token',
  namespace: 'api',
  headers: headers
});
