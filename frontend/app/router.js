import Ember from 'ember';
import config from './config/environment';

const Router = Ember.Router.extend({
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
