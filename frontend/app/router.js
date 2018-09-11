import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('about');
  this.route('login');
  this.route('knots', function() {
    this.route('create');
    this.route('show', { path: '/show/:id' });
    this.route('edit', { path: '/edit/:id' });
    this.route('delete', { path: '/delete/:id'});
  });
});

export default Router;
