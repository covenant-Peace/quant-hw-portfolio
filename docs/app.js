// Portfolio site — reads docs/projects.json and renders the showcase + live progress.
// No build step, no dependencies: edit projects.json and this page updates.

const STATUS_LABEL = { planned: "Planned", "in-progress": "In progress", complete: "Complete" };
const state = { data: null, track: "all", level: "all", status: "all" };

async function load() {
  try {
    const res = await fetch("projects.json", { cache: "no-store" });
    state.data = await res.json();
    render();
  } catch (e) {
    document.getElementById("board").innerHTML =
      `<div class="empty">Could not load <code>projects.json</code>.<br/>${e}</div>`;
  }
}

function trackById(id) {
  return state.data.tracks.find((t) => t.id === id) || { label: id, color: "#888", blurb: "" };
}
function levelById(id) {
  return state.data.levels.find((l) => l.id === id) || { label: id, note: "" };
}

function render() {
  renderOwner();
  renderOverview();
  renderControls();
  renderBoard();
}

function renderOwner() {
  const o = state.data.owner, m = state.data.meta;
  document.getElementById("owner-name").textContent = o.name;
  document.getElementById("owner-tagline").textContent = o.tagline;
  document.getElementById("owner-summary").textContent = o.summary;

  const links = [];
  if (o.github) links.push(["GitHub", `https://github.com/${o.github}`]);
  if (o.linkedin) links.push(["LinkedIn", o.linkedin]);
  if (o.email) links.push(["Email", `mailto:${o.email}`]);
  document.getElementById("owner-links").innerHTML = links
    .map(([t, h]) => `<a href="${h}" target="_blank" rel="noopener">${t}</a>`)
    .join("");

  const months = monthsBetween(m.startDate, m.targetDate);
  const elapsed = Math.max(0, monthsBetween(m.startDate, today()));
  document.getElementById("timeline").innerHTML = `
    <div class="pill"><span>Started</span><strong>${m.startDate}</strong></div>
    <div class="pill"><span>Target</span><strong>${m.targetDate}</strong></div>
    <div class="pill"><span>Elapsed</span><strong>${elapsed} / ${months} mo</strong></div>`;
}

function renderOverview() {
  const projects = state.data.projects;
  const done = projects.filter((p) => p.status === "complete").length;
  const pct = projects.length ? Math.round((done / projects.length) * 100) : 0;

  const ring = document.getElementById("overall-ring");
  ring.style.background = `conic-gradient(var(--done) ${pct * 3.6}deg, var(--border-soft) 0deg)`;
  ring.innerHTML = `<span class="ring-inner">${done}/${projects.length}</span>`;
  document.getElementById("overall-pct").textContent = pct + "%";
  document.getElementById("overall-count").textContent = `${done} / ${projects.length} projects complete`;

  document.getElementById("track-stats").innerHTML = state.data.tracks
    .map((t) => {
      const list = projects.filter((p) => p.track === t.id);
      const d = list.filter((p) => p.status === "complete").length;
      const prog = list.filter((p) => p.status === "in-progress").length;
      const p = list.length ? Math.round((d / list.length) * 100) : 0;
      return `<div class="track-card" style="--accent:${t.color}">
        <h3>${t.label}</h3>
        <p class="blurb">${t.blurb}</p>
        <div class="bar"><i style="width:${p}%"></i></div>
        <div class="count">${d} done${prog ? ` · ${prog} in progress` : ""} · ${list.length} total</div>
      </div>`;
    })
    .join("");

  document.getElementById("level-matrix").innerHTML = state.data.levels
    .map((l) => {
      const list = projects.filter((p) => p.level === l.id);
      const d = list.filter((p) => p.status === "complete").length;
      return `<div class="level-chip">
        <div class="head"><b>${l.label}</b><em>${d}/${list.length}</em></div>
        <p>${l.note}</p>
      </div>`;
    })
    .join("");
}

function renderControls() {
  const mk = (key, items, el) => {
    el.innerHTML = items
      .map((it) => {
        const active = state[key] === it.id ? "active" : "";
        const style = it.color ? `style="--accent:${it.color}"` : "";
        return `<button class="chip ${active}" ${style} data-key="${key}" data-id="${it.id}">${it.label}</button>`;
      })
      .join("");
  };
  mk("track", [{ id: "all", label: "All tracks" }, ...state.data.tracks], document.getElementById("filter-track"));
  mk("level", [{ id: "all", label: "All levels" }, ...state.data.levels], document.getElementById("filter-level"));
  mk("status", [
    { id: "all", label: "Any status" },
    { id: "complete", label: "Complete" },
    { id: "in-progress", label: "In progress" },
    { id: "planned", label: "Planned" },
  ], document.getElementById("filter-status"));

  document.querySelectorAll(".chip").forEach((c) =>
    c.addEventListener("click", () => {
      state[c.dataset.key] = c.dataset.id;
      renderControls();
      renderBoard();
    })
  );
}

function renderBoard() {
  const list = state.data.projects.filter(
    (p) =>
      (state.track === "all" || p.track === state.track) &&
      (state.level === "all" || p.level === state.level) &&
      (state.status === "all" || p.status === state.status)
  );
  const order = { "in-progress": 0, complete: 1, planned: 2 };
  list.sort((a, b) => (order[a.status] - order[b.status]) || a.level.localeCompare(b.level));

  const board = document.getElementById("board");
  if (!list.length) {
    board.innerHTML = `<div class="empty">No projects match these filters yet.</div>`;
    return;
  }
  board.innerHTML = list.map(card).join("");
}

function card(p) {
  const t = trackById(p.track);
  const lvl = levelById(p.level);
  const skills = (p.skills || []).map((s) => `<span>${s}</span>`).join("");
  const metrics = (p.metrics && p.metrics.length) ? `<p class="metrics">▸ ${p.metrics.join(" · ")}</p>` : "";
  const links = [];
  if (p.repo) links.push(`<a href="${p.repo}" target="_blank" rel="noopener">Code</a>`);
  if (p.writeup) links.push(`<a href="${p.writeup}" target="_blank" rel="noopener">Write-up</a>`);
  if (p.demo) links.push(`<a href="${p.demo}" target="_blank" rel="noopener">Demo</a>`);
  const dates = p.completed ? `✔ ${p.completed}` : (p.started ? `▶ ${p.started}` : "");

  return `<article class="card" style="--accent:${t.color}">
    <div class="meta-row">
      <span class="tag track">${t.label}</span>
      <span class="tag level">${lvl.label}</span>
      <span class="status ${p.status}"><span class="dot"></span>${STATUS_LABEL[p.status] || p.status}</span>
    </div>
    <h2>${p.title}</h2>
    <p class="desc">${p.summary}</p>
    ${p.whyItMatters ? `<p class="why">${p.whyItMatters}</p>` : ""}
    ${metrics}
    <div class="skills">${skills}</div>
    <div class="card-foot">
      ${links.join("") || '<span class="dates" style="margin-left:0;color:var(--text-faint)">Not started</span>'}
      ${dates ? `<span class="dates">${dates}</span>` : ""}
    </div>
  </article>`;
}

// --- date helpers ---
function today() { return new Date().toISOString().slice(0, 10); }
function monthsBetween(a, b) {
  const d1 = new Date(a), d2 = new Date(b);
  return (d2.getFullYear() - d1.getFullYear()) * 12 + (d2.getMonth() - d1.getMonth());
}

load();
