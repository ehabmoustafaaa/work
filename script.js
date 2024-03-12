function addTask() {
    var input = document.getElementById("taskInput");
    var taskText = input.value.trim();

    if (taskText !== "") {
        var taskList = document.getElementById("taskList");

        var taskItem = document.createElement("li");
        taskItem.innerHTML = taskText;

        taskItem.addEventListener("click", function () {
            this.classList.toggle("completed");
        });

        var deleteButton = document.createElement("button");
        deleteButton.innerHTML = "Delete";
        deleteButton.className = "delete-btn";

        deleteButton.addEventListener("click", function () {
            taskList.removeChild(taskItem);
        });

        taskItem.appendChild(deleteButton);
        taskList.appendChild(taskItem);

        input.value = "";
    }
}
