<template>
  <div>
    <modal name="xxx">
      hello, world!
    </modal>
    <!--Stats cards-->
    <div class="row">
      <div class="col-lg-3 col-sm-6" v-for="stats in statsCards">
        <stats-card>
          <div class="icon-big text-center" :class="`icon-${stats.type}`" slot="header">
            <i :class="stats.icon"></i>
          </div>
          <div class="numbers" slot="content">
            <p>{{stats.title}}</p>
            {{stats.value}}
          </div>
          <div class="stats" slot="footer">
            <i :class="stats.footerIcon"></i> {{stats.footerText}}
          </div>
        </stats-card>
      </div>
    </div>

    <div class="row">

        <div class="col-lg-6">
          <chart-card :chart-data="usersChart.data" :chart-options="usersChart.options">
            <h4 class="title" slot="title">Vehicles on road (micro-trend)</h4>
            <span slot="subTitle"> 24 Hours performance</span>
            <span slot="footer">
              <i class="ti-reload"></i> Updated 3 minutes ago</span>
            <div slot="legend">
              <i class="fa fa-circle text-info"></i> Vehicle
            </div>
          </chart-card>
        </div>

      <div class="col-lg-6">
        <div class="card">
          <paper-table :title="table.title" :sub-title="table.subTitle" :data="table.data" :columns="table.columns">
          </paper-table>
        </div>
      </div>

      <!--Charts-->
      <!-- <div class="row"> -->


<!-- 
        <div class="col-md-6 col-xs-12">
          <chart-card :chart-data="preferencesChart.data"  chart-type="Pie">
            <h4 class="title" slot="title">Email Statistics</h4>
            <span slot="subTitle"> Last campaign performance</span>
            <span slot="footer">
              <i class="ti-timer"></i> Campaign set 2 days ago</span>
            <div slot="legend">
              <i class="fa fa-circle text-info"></i> Open
              <i class="fa fa-circle text-danger"></i> Bounce
              <i class="fa fa-circle text-warning"></i> Unsubscribe
            </div>
          </chart-card>
        </div>

        <div class="col-md-6 col-xs-12">
          <chart-card :chart-data="activityChart.data" :chart-options="activityChart.options">
            <h4 class="title" slot="title">2015 Sales</h4>
            <span slot="subTitle"> All products including Taxes</span>
            <span slot="footer">
              <i class="ti-check"></i> Data information certified</span>
            <div slot="legend">
              <i class="fa fa-circle text-info"></i> Tesla Model S
              <i class="fa fa-circle text-warning"></i> BMW 5 Series
            </div>
          </chart-card>
        </div> -->

    </div>
  </div>
</template>
<script>
  import StatsCard from 'components/UIComponents/Cards/StatsCard.vue'
  import ChartCard from 'components/UIComponents/Cards/ChartCard.vue'
  import PaperTable from 'components/UIComponents/PaperTable.vue'

  const tableColumns = ['Id', 'Name', 'Location', 'Time', 'GPS']
  const tableData = [
    {
      id: 1,
      name: 'Road accident',
      location: 'Jalan PJS 11/20',
      time: '9:32 AM, 29/10/17',
      gps: '3.068331, 101.602162'
    },
    {
      id: 2,
      name: 'Robbery',
      location: 'Jalan Universiti',
      time: '9:57 AM, 29/10/17',
      gps: '3.067661, 101.603634'
    },
    {
      id: 3,
      name: 'Street Demonstrations',
      location: 'Persiaran Lagoon',
      time: '10:13 AM, 29/10/17',
      gps: '3.072813, 101.608980'
    }]
  export default {
    components: {
      StatsCard,
      ChartCard,
      PaperTable
    },
    /**
     * Chart data used to render stats, charts. Should be replaced with server data
     */
    data () {
      return {
        statsCards: [
          {
            type: 'warning',
            icon: 'ti-car',
            title: 'Vehicles on road',
            value: '698',
            footerText: 'Updated 5 mins ago',
            footerIcon: 'ti-reload'
          },
          {
            type: 'success',
            icon: 'ti-light-bulb',
            title: 'Traffic light count',
            value: '29',
            footerText: 'Last day',
            footerIcon: 'ti-calendar'
          },
          {
            type: 'danger',
            icon: 'ti-pulse',
            title: 'Emergency Cases',
            value: '3',
            footerText: 'In the last hour',
            footerIcon: 'ti-timer'
          },
          {
            type: 'info',
            icon: 'ti-cloud',
            title: 'Weather',
            value: '27°C',
            footerText: 'Updated 15 mins ago',
            footerIcon: 'ti-reload'
          }
        ],
        usersChart: {
          data: {
            labels: ['5:00AM', '6:00AM', '7:00AM', '8:00AM', '9:00AM', '10:00AM', '11:00AM'],
            series: [
              [202, 585, 890, 1262, 1094, 726, 698]
            ]
          },
          options: {
            low: 0,
            high: 1500,
            showArea: true,
            height: '245px',
            axisX: {
              showGrid: false
            },
            lineSmooth: this.$Chartist.Interpolation.simple({
              divisor: 3
            }),
            showLine: true,
            showPoint: false
          }
        },
        activityChart: {
          data: {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            series: [
              [542, 543, 520, 680, 653, 753, 326, 434, 568, 610, 756, 895],
              [230, 293, 380, 480, 503, 553, 600, 664, 698, 710, 736, 795]
            ]
          },
          options: {
            seriesBarDistance: 10,
            axisX: {
              showGrid: false
            },
            height: '245px'
          }
        },
        preferencesChart: {
          data: {
            labels: ['62%', '32%', '6%'],
            series: [62, 32, 6]
          },
          options: {}
        },
        table: {
          title: 'Emergency Cases',
          // subTitle: 'Here is a subtitle for this table',
          columns: [...tableColumns],
          data: [...tableData]
        }
      }
    },
    created () {
      const modal = this.$modal
      const ws = new WebSocket('ws://localhost:9080')

      ws.onopen = function () {
        console.log('Opening')
      }

      ws.onmessage = function (evt) {
        const receivedMsg = evt.data
        modal.show('xxx')
        console.log(receivedMsg)
        alert(receivedMsg)
      }

      ws.onclose = function () {
        console.log('Closing')
      }

      ws.onerror = function () {
        console.log('Error occured')
        ws.close()
      }

      window.onbeforeunload = function (event) {
        ws.close()
      }
    }
  }

</script>
<style>

</style>
