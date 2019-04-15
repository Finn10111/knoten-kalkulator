import Controller from '@ember/controller';
import { inject } from '@ember/service';

export default Controller.extend({
  session: inject('session'),

  actions: {
    authenticate: function() {
      var credentials = this.getProperties('identification', 'password'),
      authenticator = 'authenticator:jwt';
      this.get('session').authenticate(authenticator, credentials);
    }
  }
});
