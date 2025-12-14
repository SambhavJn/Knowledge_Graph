const svg = d3.select("svg");
const width = 1000, height = 1000;

const simulation = d3.forceSimulation()
    .force("link", d3.forceLink().id(d => d.id).distance(120))
    .force("charge", d3.forceManyBody().strength(-300))
    .force("center", d3.forceCenter(width / 2, height / 2));

function draw() {
    fetch("/graph")
        .then(r => r.json())
        .then(data => {
            svg.selectAll("*").remove();

            const link = svg.selectAll("line")
                .data(data.edges)
                .enter().append("line")
                .attr("stroke", "#aaa");

            const node = svg.selectAll("circle")
                .data(data.nodes)
                .enter().append("circle")
                .attr("r", 10)
                .attr("fill", "steelblue");

            const label = svg.selectAll("text")
                .data(data.nodes)
                .enter().append("text")
                .text(d => d.id)
                .attr("dx", 12)
                .attr("dy", 4);

            simulation.nodes(data.nodes).on("tick", () => {
                link
                    .attr("x1", d => d.source.x)
                    .attr("y1", d => d.source.y)
                    .attr("x2", d => d.target.x)
                    .attr("y2", d => d.target.y);

                node
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y);

                label
                    .attr("x", d => d.x)
                    .attr("y", d => d.y);
            });

            simulation.force("link").links(data.edges);
            simulation.alpha(1).restart();
        });
}

function addRelation() {
    fetch("/add", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            entity1: e1.value,
            relationship: rel.value,
            entity2: e2.value
        })
    }).then(draw);
}

function uploadCSV() {
    const f = document.getElementById("csv").files[0];
    const fd = new FormData();
    fd.append("file", f);

    fetch("/upload", { method: "POST", body: fd })
        .then(draw);
}

function queryGraph() {
    fetch(`/query?entity=${query.value}`)
        .then(r => r.json())
        .then(d => result.innerText = JSON.stringify(d, null, 2));
}

draw();


