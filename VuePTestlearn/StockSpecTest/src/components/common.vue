<script type="text/javascript">
    const spec_dict = ...
    function getDisplayValueScope(scope) {
      var name = scope.column.property
      var value = scope.row[scope.column.property]
      return getDisplayValue(name,value)
    }

    function getDisplayValue(name,value) {
      
    }
    export default {
        spec_dict,
        getDisplayValueScope,
        getDisplayValue
    }
</script>