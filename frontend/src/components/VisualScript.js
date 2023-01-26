const url = 'http://127.0.0.1:5000/heatmap'

export const getHeatmap = async (start_date = null, end_date = null) => {
    try {
        let heatmapUrl = url;
        /* TODO: validate if correct dates are passed */
        // if (start_date === 'None' && end_date === 'None') {
        heatmapUrl += '/' + start_date + '/' + end_date;
        console.log(heatmapUrl);

        const response = await fetch(heatmapUrl)
        return await response.text();
    } catch (err) {
        console.error(err)
    }
}
