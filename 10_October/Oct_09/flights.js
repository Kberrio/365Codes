const express = require('express');
const Flight = require('../models/Flight');
const router = express.Router();

// Create a flight
router.post('/', async (req, res) => {
  try {
    const flight = new Flight(req.body);
    await flight.save();
    res.status(201).send(flight);
  } catch (err) {
    res.status(400).send(err);
  }
});

// Get all flights
router.get('/', async (req, res) => {
  try {
    const flights = await Flight.find();
    res.send(flights);
  } catch (err) {
    res.status(500).send(err);
  }
});

// Get a flight by ID
router.get('/:id', async (req, res) => {
  try {
    const flight = await Flight.findById(req.params.id);
    if (!flight) {
      return res.status(404).send();
    }
    res.send(flight);
  } catch (err) {
    res.status(500).send(err);
  }
});

// Update a flight by ID
router.put('/:id', async (req, res) => {
  try {
    const flight = await Flight.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
      runValidators: true
    });
    if (!flight) {
      return res.status(404).send();
    }
    res.send(flight);
  } catch (err) {
    res.status(400).send(err);
  }
});

// Delete a flight by ID
router.delete('/:id', async (req, res) => {
  try {
    const flight = await Flight.findByIdAndDelete(req.params.id);
    if (!flight) {
      return res.status(404).send();
    }
    res.send(flight);
  } catch (err) {
    res.status(500).send(err);
  }
});

module.exports = router;
