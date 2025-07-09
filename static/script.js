document.getElementById('generate-btn').addEventListener('click', async () => {
    const res = await fetch('/generate', { method: 'POST' });
    const data = await res.json();

    if (data.success) {
        document.getElementById('tweet-text').value = data.tweet;
        document.getElementById('post-btn').disabled = false;
    } else {
        alert(`Error: ${data.error}`);
    }
});

document.getElementById('post-btn').addEventListener('click', async () => {
    const tweet = document.getElementById('tweet-text').value;

    const res = await fetch('/post', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ tweet }),
    });

    const data = await res.json();

    if (data.success) {
        alert('✅ Tweet posted successfully!');
    } else {
        alert(`❌ Error: ${data.error}`);
    }
});

document.getElementById('tweet-text').addEventListener('input', (e) => {
    const count = e.target.value.length;
    document.getElementById('char-count').innerText = `${count}/250`;
});
