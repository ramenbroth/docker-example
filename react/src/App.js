import React, { useState, useEffect } from 'react';
import './App.css';

export default (() => {
  const [test, setTest] = useState([]);
  useEffect(() => {
    fetch("test")
      .then(res => res.json())
      .then(data => setTest(data.customers));
  }, []);
  return (
    <div className="App">
      Customers:
      {test.map(val => val)}
    </div>
  );
})
