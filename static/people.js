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

function del(id, callback) {
    fetch('/' + id, {
        method: 'DELETE'
    }).then(callback);
}

Vue.component('date-input', {
    props: ['value', 'placeholder'],
    template: `
        <input ref="input" type="text" v-bind:placeholder="placeholder"
               v-model="displayValue"
               v-on:blur="update($event.target.value)">`,
    data: function () {
        return {
            isActive: false,
            lastValue: this.value
        }
    },
    computed: {
        displayValue: function () {
            return moment(this.value, 'YYYY-MM-DD').format('l');
        }
    },
    methods: {
        update: function (value) {
            var formattedValue = moment(value, 'MM/DD/YYYY');
            var newValue = formattedValue.isValid() ? formattedValue.format('YYYY-MM-DD') : this.lastValue;
            if (formattedValue !== value) {
                this.$refs.input.value = this.displayValue;
            }
            if (newValue === this.lastValue) return;
            this.lastValue = newValue;
            this.$emit('input', newValue);
            this.$emit('update');
        }
    }
});

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
            add(newperson, function (id) {
                model.people.push(newperson);
                newperson.id = id;
            });
        },
        del: function (person) {
            del(person.id, function () {
                model.people = model.people.filter(function (e) {
                    return e.id !== person.id;
                });
            });
        }
    }
});
