<template>
  <FullCalendar :options="calendarOptions" />
</template>
<script>
import FullCalendar from '@fullcalendar/vue3'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'
import interactionPlugin from '@fullcalendar/interaction'
export default {
  components: { FullCalendar },
  data() {
    return {
      calendarOptions: {
        plugins: [dayGridPlugin, interactionPlugin, timeGridPlugin],
        initialView: 'timeGridWeek',
        dateClick: this.handleDateClick,
        events: [
          { title: 'event 1', date: '2024-01-01' },
          { title: 'event 2', start: '2024-01-07T10:30:00', end: '2024-01-09T11:30:00' }
        ],
        headerToolbar: {
          start: 'dayGridMonth,timeGridWeek,timeGridDay',
          center: 'title',
          end: 'prevYear,prev,next,nextYear'
        }
      }
    }
  },
  setup() {},
  created() {},
  mounted() {},
  unmounted() {},
  methods: {
    handleDateClick: function (arg) {
      console.log(arg)
      // alert('date click! ' + arg.dateStr)
    }
  }
}
</script>
