<template>
    <div>
        <div id="allmap"></div>
    </div>
</template>

<script>
    export default {
        name: "baidumap",
        props: {
            points: {
                type: Array,
                required: true
            },
        },
        data() {
            return {
                arrayList: [],
                pois: this.points,

            };
        },
        watch: {
            points: {
                immediate: true, // 这句重要
                handler(val) {
                    this.BaiduMap()
                },
            },
        },
        methods: {
            BaiduMap() {
                // 百度地图API功能
                var map = new BMap.Map("allmap");
                map.centerAndZoom(new BMap.Point(113.552724, 22.255899), 13);
                map.enableScrollWheelZoom(true);
                map.addControl(new BMap.NavigationControl(BMAP_ANCHOR_TOP_LEFT));
                function showPoly(pointList) {
                    //循环显示点对象
                    for (var c = 0; c < pointList.length; c++) {
                        var marker = new BMap.Marker(pointList[c]);
                        map.addOverlay(marker);
                        //将途经点按顺序添加到地图上
                        var label = new BMap.Label(c + 1, { offset: new BMap.Size(20, -10) });
                        marker.setLabel(label);
                    }
                }
                //将百度坐标点放入数据中
                this.arrayList = [];
                for (let i = 0; i < this.points.length; i++) {
                    let tmp1 = this.points[i]["lng"];
                    let tmp2 = this.points[i]["lat"];
                    var p = new BMap.Point(tmp1, tmp2);
                    this.arrayList.push(p);
                }

                //显示轨迹

                showPoly(this.arrayList);
            }
        },
        mounted() {
            this.$nextTick(() => {
                var timer = setTimeout(() => {
                    this.BaiduMap();
                }, 500);
            });
        }
    };
</script>

<style>
    body,
    html,
    #allmap {
        width: 100%;
        height: 340px;
        margin-bottom: 50px;
        font-family: "微软雅黑";
        z-index: -1;
    }
</style>