const CSRFToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
const postHeaders = {'Content-type': 'application/json', 'X-CSRFToken': CSRFToken}



async function get_actions_in_year() {
    let year = document.querySelector('.calendar_header').textContent
    let response = await fetch(`/api/get_get_actions_in_year/${year}/`, {method: 'GET'})
    let info = await response.json()
    for (let key in info) {
        let elem = document.querySelector(`td[data-value="${key}"]`)
        let actions = info[key]
        if (actions.length == 1) {
            elem.style.backgroundColor = '#E2EFDA'
        } else if (actions.length == 2) {
            elem.style.backgroundColor = '#C6E0B4'
        } else if (actions.length > 2) {
            elem.style.backgroundColor = '#A9D08E'
        }
        elem.setAttribute('title', actions.join(', '))
    }
}

get_actions_in_year()