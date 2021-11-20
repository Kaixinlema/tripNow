<template>
    <baidu-map class="map" :center="center" :zoom="zoom" @click="pointSetClick" :scroll-wheel-zoom="true"
        @ready="handler">

        <bm-scale anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-scale>
        <bm-local-search :keyword="keyword" zoom="12.8" v-bind:auto-viewport="true"></bm-local-search>
        <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>

        <bm-marker v-for="(item,index) in mapObj" :key="index" :position="item"
            :animation="draggingList[index]?'BMAP_ANIMATION_BOUNCE':''" @click="showItem(index)">
            <bm-label :content="item.title" :labelStyle="{color: 'red', fontSize : '20px'}"
                :offset="{width: -35, height: 30}" />
        </bm-marker>
        <!-- <bml-marker-clusterer averageCenter>
            <div v-for="obj in infowindowsinformation">
     
              <bm-marker :title="obj.code"
                         :position="{lng: obj.lng[0],lat: obj.lat[0]}"
                         @click="openinformation(this,obj)" v-if="bmlmark">
                <bm-info-window :show="obj.infoWindowShow" class="bminfowindow"
                                @close="closeinformation(this,obj)">
                  <p>{{ infowindowstitle }}</p>
                  <p v-for="(value,key,num) in obj" v-if="value[1]">
                    {{ key === 'lat' || key === 'lng' ? (key === 'lat' ? '地理纬度' : '地理经度') : key }}:{{ value[0] }}
                  </p>
                </bm-info-window>
              </bm-marker>
            </div>
          </bml-marker-clusterer> -->
        <bm-info-window :position="position" :show="show" @close="infoWindowClose" @open="infoWindowOpen">
            <div>地点： {{position.title}}</div>
        </bm-info-window>
    </baidu-map>
</template>
<script>

    export default {
        name: 'Try',
        props: {
            mapObj: Array,//结构[{ lng: '', lat: '',title:''}]
            showMap: Boolean,
        },
        watch: {
            showMap() {
                this.center = ''
                this.initMaker()
            },
        },
        data() {
            return {
                draggingList: [],
                position: { lng: '', lat: '', title: '' },
                center: { lng: '', lat: '' },
                zoom: 16,
                show: false,
                geoc: {},
                map: {},
            }
        },
        mounted() { },
        methods: {
            showItem(item) {
                this.draggingList = []
                this.draggingList[item] = true
                this.position = this.mapObj[item]
                this.show = true
            },
            infoWindowClose() {
                this.show = false
            },
            infoWindowOpen() {
                this.show = true
            },
            handler({ BMap, map }) {
                var geoc = new BMap.Geocoder()
                this.geoc = geoc
                map = new BMap.Map('dituContent')
                this.map = map
            },
            //初始化，每次定位到第一个点的位置
            initMaker() {
                if (this.mapObj.length) {
                    this.draggingList[0] = true
                    this.center = this.mapObj[0]
                }
                this.zoom = 16
            },
            pointSetClick(e) {
                this.geoc.getLocation(e.point, function (rs) {
                    var addComp = rs.addressComponents
                    console.log(rs)
                    console.log(
                        addComp.province +
                        '-' +
                        addComp.city +
                        '-' +
                        addComp.district +
                        '-' +
                        addComp.street +
                        '-' +
                        addComp.streetNumber
                    )
                })
            },
        },
    }
</script>

<style>
    /* The container of BaiduMap must be set width & height. */
    .map {
        width: 768px;
        height: 600px;
    }
</style>