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
          <p>Games Library 🕹️</p>
          <hr />
          <br />
          <!-- Alert Message -->
          <button type="button" class="btn btn-success btn-sm">add Game</button>
          <br /><br />
          <table class="table table-hover">
            <!-- Table Header -->
            <thead>
              <tr>
                <th scope="col">Title</th>
                <th scope="col">Genre</th>
                <th scope="col">Plate?</th>
                <th scope="col">Player</th>
                <th scope="col">Actions</th>
              </tr>
            </thead>
            <!-- Table Body -->
            <tbody></tbody>
            <tr>
              <td>Game 1</td>
              <td>Genre 1</td>
              <td>Yes</td>
              <td>Player 1</td>
              <td class="btn-group" role="group">
                <button type="button" class="btn btn-info btn-sm">Edit</button>
                <button type="button" class="btn btn-danger btn-sm">
                  Delete
                </button>
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "GamesLibraryComponent",
};
</script>
