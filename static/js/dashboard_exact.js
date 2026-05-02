document.addEventListener("DOMContentLoaded", function () {
  var el = document.getElementById("dashboard-data");
  if (!el) return;

  var payload = {};
  try {
    payload = JSON.parse(el.dataset.payload || "{}");
  } catch (_) {
    payload = {};
  }

  var labels = payload.line_labels || [];
  var fraud = payload.fraud_trend || [];
  var legit = payload.legit_trend || [];
  var pie = payload.pie_data || [0, 0];

  var lineCanvas = document.getElementById("fraudLineChart");
  if (lineCanvas && window.Chart) {
    new Chart(lineCanvas, {
      type: "line",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Fraud Cases",
            data: fraud,
            borderColor: "#ef4444",
            backgroundColor: "rgba(239,68,68,0.15)",
            fill: true,
            tension: 0.35
          },
          {
            label: "Safe Cases",
            data: legit,
            borderColor: "#22c55e",
            backgroundColor: "rgba(34,197,94,0.15)",
            fill: true,
            tension: 0.35
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: { y: { beginAtZero: true } }
      }
    });
  }

  var pieCanvas = document.getElementById("fraudPieChart");
  if (pieCanvas && window.Chart) {
    new Chart(pieCanvas, {
      type: "doughnut",
      data: {
        labels: ["Fraud", "Safe"],
        datasets: [{ data: pie, backgroundColor: ["#ef4444", "#22c55e"] }]
      },
      options: { responsive: true, maintainAspectRatio: false }
    });
  }
});
