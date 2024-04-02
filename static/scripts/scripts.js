function saveSelectionToLocalStorage(startDate, endDate, adults, children) {
    const reservationData = JSON.stringify({
        startDate: startDate,
        endDate: endDate,
        adults: adults,
        children: children
    });
    localStorage.setItem('reservationData', reservationData);
}



function readSelectionFromLocalStorage() {
    const reservationData = JSON.parse(localStorage.getItem('reservationData'));
    if (reservationData) {
        console.log('Read reservation data:', reservationData);
        // Here, you can assign the read values to form elements or perform other actions.
    } else {
        console.log('No saved reservation data found.');
    }
}
