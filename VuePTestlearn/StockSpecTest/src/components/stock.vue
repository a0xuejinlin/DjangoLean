<template>
  <div>
<el-row :gutter="10">
    <el-col :span="4">贝塔系数(年)</el-col>
    <el-col :span="4"><router-link :to="{ path: 'stockspec', query: {specname: 'beta_y', order:'asc', abs:true}}">最小</router-link></el-col>
    <el-col :span="4"><router-link :to="{ path: 'stockspec', query: {specname: 'beta_y', order:'desc', abs:true}}">最大</router-link></el-col>
</el-row>
<el-row>
...
<el-row>
</div>
</template>