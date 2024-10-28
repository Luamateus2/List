document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.querySelector('.calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        plugins: ['dayGrid'],
        initialView: 'dayGridMonth',
        events: [
            { title: 'Evento 1', date: '2024-10-01' },
            { title: 'Evento 2', date: '2024-10-15' },
            { title: 'Evento 3', date: '2024-10-20' }
        ]
    });

    calendar.render();
});
