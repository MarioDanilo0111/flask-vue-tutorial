<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- Bootstrap CDN -->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
        integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1
            class="text-center bg-primary text-white"
            style="border-radius: 10px"
          >
            Games Library 🕹️
          </h1>
          <hr />
          <br />
          <!-- Alert Message -->
          <b-alert
            variant="success"
            :show="showMessage"
            @dismissed="showMessage = false"
          >
            {{ message }}
          </b-alert>
          <button
            type="button"
            class="btn btn-success btn-sm"
            v-b-modal.game-modal
          >
            add Game
          </button>
          <br /><br />
          <table class="table table-hover">
            <!-- Table Header -->
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Plate?</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <!-- Table Body -->
            <tbody>
              <tr v-for="(game, index) in games" :key="index">
                <td>{{ game.title }}</td>
                <td>{{ game.genre }}</td>
                <td>
                  <span v-if="game.played">Yes</span>
                  <span v-else>No</span>
                </td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info btn-sm">
                      Edit
                    </button>
                    <button type="button" class="btn btn-danger btn-sm">
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer
            class="bg-primary text-white text-center"
            style="border-radius: 10px"
          >
            Copyright &copy;. All Rights Reserved 2024
          </footer>
        </div>
      </div>

      <!--  First Modal -->
      <b-modal
        ref="addGameModal"
        id="game-modal"
        title="Add a new Game"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-title-group"
            label="Title:"
            label-for="form-title-input"
          >
            <b-form-input
              id="form-title-input"
              type="text"
              v-model="addGameForm.title"
              required
              placeholder="Enter Title"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="form-genre-group"
            label="Genre:"
            label-for="form-genre-input"
          >
            <b-form-input
              id="form-genre-input"
              type="text"
              v-model="addGameForm.genre"
              required
              placeholder="Enter Genre"
            ></b-form-input>
          </b-form-group>

          <!-- Checkbox -->
          <b-form-group id="form-played-group">
            <b-form-checkbox-group
              v-model="addGameForm.played"
              id="form-checks"
            >
              <b-form-checkbox value="true"> Played? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <!-- Buttons: submit and reset -->
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger">Reset</b-button>
        </b-form>
      </b-modal>
      <!-- End First Modal -->

      <!-- Second Modal  -->

      <b-modal
        ref="editGameModal"
        id="game-update-modal"
        title="Update"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
          <b-form-group
            id="form-title-edit-group"
            label="Title:"
            label-for="form-title-edit-input"
          >
            <b-form-input
              id="form-title-edit-input"
              type="text"
              v-model="editForm.title"
              required
              placeholder="Enter Title"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="form-genre-edit-group"
            label="Genre:"
            label-for="form-genre-edit-input"
          >
            <b-form-input
              id="form-genre-edit-input"
              type="text"
              v-model="editForm.genre"
              required
              placeholder="Enter Genre"
            ></b-form-input>
          </b-form-group>

          <!-- Checkbox -->
          <b-form-group id="form-played-edit-group">
            <b-form-checkbox-group v-model="editForm.played" id="form-checks">
              <b-form-checkbox value="true"> Played? </b-form-checkbox>
            </b-form-checkbox-group>
          </b-form-group>
          <!-- Buttons: submit and reset -->
          <b-button type="submit" variant="outline-info">Update</b-button>
          <b-button type="reset" variant="outline-danger">Cancel</b-button>
        </b-form>
      </b-modal>

      <!-- End Second Modal -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      games: [],
      addGameForm: {
        title: "",
        genre: "",
        played: [], //is an array cause it's a checkbox
      },
      message: "",
      showMessage: false,
    };
  },

  methods: {
    // GET Function
    getGames() {
      const path = "http://localhost:5001/games";
      axios
        .get(path)
        .then((res) => {
          console.log("Respons data: ", res.data);
          this.games = res.data.games;
        })
        .catch((err) => {
          console.error("Error fetching games: ", err);
        });
    },

    // Post Function
    addGame(payload) {
      const path = "http://localhost:5001/games";
      axios
        .post(path, payload)
        .then(() => {
          this.getGames();
          this.message = "Game Added Successfully!";
          this.showMessage = true;
          setTimeout(() => {
            this.showMessage = false;
          }, 3000);
        })
        .catch((err) => {
          console.error("Error fetching games: ", err);
          this.getGames();
        });
    },
    initForm() {
      this.addGameForm.title = "";
      this.addGameForm.genre = "";
      this.addGameForm.played = [];
    },

    onSubmit(event) {
      event.preventDefault();
      this.$refs.addGameModal.hide();
      let played = false;
      if (this.addGameForm.played[0]) played = true;
      const payload = {
        title: this.addGameForm.title,
        genre: this.addGameForm.genre,
        played,
      };
      this.addGame(payload);
      this.initForm();
    },

    onReset(event) {
      event.preventDefault();
      this.$refs.addGameModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getGames();
  },
};
</script>
