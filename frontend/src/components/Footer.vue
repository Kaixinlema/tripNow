<template>
    <div>
        <div class="footerSet">
            <el-row :gutter="20">
                <el-col :span="8">
                    <div class="footerIcon"></div>
                    <p>TripNow为你推荐操作简单、自定义的旅游计划。</p>
                </el-col>
                <el-col :span="4">
                    <h4>关于我们</h4>
                    <p>团队详情</p>
                    <p>详细介绍</p>
                    <p>主要产品</p>
                    <p>联系我们</p>
                </el-col>
                <el-col :span="4">
                    <h4>使用条款</h4>
                    <p>隐私条款</p>
                    <p>服务条款</p>
                </el-col>
                <el-col :span="4">
                    <h4>相关信息</h4>
                    <p>事件</p>
                    <p>出版</p>
                    <p>职业</p>
                    <p>Blog</p>
                </el-col>
                <el-col :span="4">
                    <h4>关注我们<i class="el-icon-share"></i></h4>
                    <el-row>
                        <el-col :span="8">
                            <div class="my-icon-wechat"></div>
                        </el-col>
                        <el-col :span="8">
                            <div class="my-icon-ins"></div>
                        </el-col>
                        <el-col :span="8">
                            <div class="my-icon-face"></div>
                        </el-col>
                    </el-row>
                </el-col>
            </el-row>
        </div>
        <div class="rightRes">
            <span>© 2021 TripNow 版权所有</span>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Footer",
    };
</script>

<style>
    .footerSet {
        text-align: left;
        font-size: 12px;
        background-color: #E9EEF3;
        color: #333;
        border-radius: 1px;
        box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
        padding: 60px 60px 20px 60px;
    }

    .footerIcon {
        width: 150px;
        height: 60px;
        background-image: url(../assets/ZHimg/icon-black.png);
        background-size: cover;
    }

    .rightRes {
        width: 100%;
        font-size: 12px;
        text-align: center;
        background-color: lightgray;
        line-height: 40px;
    }

    .my-icon-wechat {
        width: 30px;
        height: 30px;
        background: url(../assets/ZHimg/wechat.png);
        background-size: cover;
    }

    .my-icon-ins {
        width: 30px;
        height: 30px;
        background: url(../assets/ZHimg/ins.png);
        background-size: cover;
    }

    .my-icon-face {
        width: 30px;
        height: 30px;
        background: url(../assets/ZHimg/face.png);
        background-size: cover;
    }
</style>