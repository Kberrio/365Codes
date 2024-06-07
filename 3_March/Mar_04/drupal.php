<?php

/**
 * Implements hook_menu().
 */
function hello_world_menu() {
  $items['hello-world'] = array(
    'title' => 'Hello World',
    'description' => 'Displays a simple Hello World message.',
    'page callback' => 'hello_world_page',
    'access callback' => TRUE,
  );

  return $items;
}

/**
 * Page callback function to display Hello World message.
 */
function hello_world_page() {
  return array(
    '#markup' => '<p>Hello World!</p>',
  );
}
