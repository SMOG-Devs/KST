const heatmap_frame = document.querySelector('.map-frame');
const url = 'http://127.0.0.1:5000/heatmap'

export const getHeatmap = async (start_date = null, end_date = null) => {
    try {
        if (start_date && end_date) {
            console.log(url + `?start_date=${start_date}&end_date=${end_date}`);
        }
        const response = await fetch(url)
        return await response.text();
        // return await response.text();
    } catch (err) {
        console.error(err)
    }
}

async function main() {
    heatmap_frame.srcdoc = await getHeatmap();
    console.log(heatmap_frame.innerHTML);
}
