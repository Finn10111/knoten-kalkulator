import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('knot-cord', 'Integration | Component | knot cord', {
  integration: true
});

test('it renders', function(assert) {

  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  this.render(hbs`{{knot-cord}}`);

  assert.equal(this.$().text().trim(), '');

  // Template block usage:
  this.render(hbs`
    {{#knot-cord}}
      template block text
    {{/knot-cord}}
  `);

  assert.equal(this.$().text().trim(), 'template block text');
});
