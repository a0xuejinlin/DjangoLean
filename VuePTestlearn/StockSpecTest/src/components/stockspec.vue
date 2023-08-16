

<el-table :data="stockSpecData" :header-cell-style="{background:'#eef1f6',color:'#606266'}" :height="tableHeight" style="width: 100%" @row-click="displayDetails">
    <el-table-column prop="code" label="代码" fixed :show-overflow-tooltip="true"></el-table-column>
    <el-table-column prop="name" label="名字" fixed :show-overflow-tooltip="true">
      <template slot-scope="scope">
        <a :href="getLink(scope.row.code)" target="_blank" class="buttonText"><div style="font-size:16">{{scope.row.name}}</div></a>
      </template>
    </el-table-column>
    <el-table-column
      v-for="(item,key) in titleData"
      :key="key"
      :prop="item.value"
      :label="item.name"
    >
      <template slot-scope="scope">
        <span>{{getDisplayValueScope(scope)}}</span>
      </template>
    </el-table-column>
  </el-table>

<el-dialog :title="selectname + '(' + selectcode + ')'" :visible.sync="dialogTableVisible" custom-class="customSize">
      <div v-if="dialogTableVisible"><candlechart :props1="candleprops"></candlechart></div>
</el-dialog>
<style>
  .customSize{
    width:70%;
    height:70%;
  }
//实现内部滚动条
 .el-dialog {
    display: flex;
    flex-direction: column;
  }
  .el-dialog__body {
    overflow: auto;
  }
</style>






<script>
getData() {
      this.specname = this.$route.query.specname;
      this.order = this.$route.query.order;
      this.abs = false;
      if(this.$route.query.abs) {
        this.abs = this.$route.query.abs
      }
}

import axios from "axios";
created() {
    this.getData();
    axios
      .get("http://127.0.0.1:8000/stockserver/spec/", {
        params: {
          specname: this.specname,
          order: this.order,
          abs: this.abs
        }
      })
      .then(response => {
        this.stockSpecData = response.data.data;
      });
}


displayDetails(row, column, event) {
      if(column.label == "名字") {
        return
      }
      this.selectcode = row.code
      this.selectname = row.name

      axios
      .get("http://127.0.0.1:8000/stockserver/dayk/", {
        params: {
          code: this.selectcode,
        }
      })
      .then(response => {
        this.dayk = response.data.data;
        this.candleprops = {
          'code':this.selectcode,
          'name':this.selectname,
          'kdata': this.dayk,
          'reladay': this.selectreladayk,
        };
        this.dialogTableVisible = true
      });
    }
</script>