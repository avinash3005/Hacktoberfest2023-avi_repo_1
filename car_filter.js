// Sample car brand data with attributes: name, seating capacity, EV, AV, RC
const carBrands = [
  { name: "Tesla Model 3", seats: 5, ev: true, av: false, rc: false },
  { name: "Toyota Camry", seats: 5, ev: false, av: false, rc: false },
  { name: "Nissan Leaf", seats: 5, ev: true, av: false, rc: false },
  { name: "Waymo One", seats: 4, ev: true, av: true, rc: false },
  { name: "Tesla Model X", seats: 7, ev: true, av: false, rc: false },
  { name: "Audi A8", seats: 5, ev: false, av: true, rc: false },
  { name: "Remote-Control Car", seats: 2, ev: false, av: false, rc: true },
];

// Function to filter cars based on criteria
function filterCars(criteria) {
  return carBrands.filter((car) => {
    return (
      (!criteria.seats || car.seats >= criteria.seats) &&
      (!criteria.ev || car.ev === criteria.ev) &&
      (!criteria.av || car.av === criteria.av) &&
      (!criteria.rc || car.rc === criteria.rc)
    );
  });
}

// Sample criteria: Filter for EVs with at least 5 seats
const criteria = {
  seats: 5,
  ev: true,
  av: false,
  rc: false,
};

// Perform the filtering
const filteredCars = filterCars(criteria);

// Display the filtered car brands
console.log("Filtered Car Brands:");
filteredCars.forEach((car) => {
  console.log(`- ${car.name}`);
});
