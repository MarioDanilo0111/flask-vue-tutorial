<template>
  <div>
    <button type="button" class="btn btn-primary">{{ msg }}</button>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "SharkComponent",

  data() {
    return {
      msg: "Shark 🦈",
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/shark";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
};
</script>
