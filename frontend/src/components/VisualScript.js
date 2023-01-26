const heatmap_frame = document.querySelector('.map-frame');
const url = 'http://127.0.0.1:5000/heatmap'

const getHeatmap = async () => {
    try {
        const response = await fetch(url)
        return await response.text();
    } catch (err) {
        console.error(err)
    }
}

async function main() {
    heatmap_frame.srcdoc = await getHeatmap();
    console.log(heatmap_frame.innerHTML);
}

main();