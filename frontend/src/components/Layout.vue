<template>
    <div>
        <h1>layout组件</h1>
        <el-row>
            <el-col :span="8">1</el-col>
            <el-col :span="8">2</el-col>
            <el-col :span="8">3</el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "Layout.vue",
    };
</script>

<style>
</style>