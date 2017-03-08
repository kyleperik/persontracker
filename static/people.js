function save_changes(person, callback, error) {
    var data = JSON.stringify(person);
    fetch('/' + person.id, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: data
    }).then(function (response) {
        if (!response.ok) {
            error();
        } else {
            callback();
        }
    });
}

function add(person, callback) {
    var data = JSON.stringify(person);
    fetch('/', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: data
    }).then(function (response) {
        return response.json()
    }).then(callback);
}

var timeout;
var myvue = new Vue({
    el: '#People',
    data: model,
    methods: {
        save_changes: function (person) {
            if (model.status === 'saving...') {
                clearTimeout(timeout);
            }
            model.status = 'saving...';
            timeout = setTimeout(function () {
                save_changes(person, function () {
                    model.status = 'changes saved';
                }, function (e) {
                    model.status = 'error saving :(';
                });
            }, 500);
        },
        add: function () {
            var newperson = {
                firstname: '',
                lastname: '',
                dateofbirth: '2000-01-01',
                zipcode: '00000'
            };
            model.people.push(newperson);
            add(newperson, function (id) {
                newperson.id = id;
            });
        }
    }
});
