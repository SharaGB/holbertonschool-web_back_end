const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

  jobs.forEach(element => {
    const job = queue.create('push_notification_code_3', element);
    job.save((err) => {
      if(!err) console.log(`Notification job created: ${job.id}`);
    });

    job.on('complete', (result) => {
      console.log(`Notification job ${job.id} completed`);
    });
  
    job.on('failed', (failed) => {
      console.log(`Notification job ${job.id} failed: ${failed}`);
    });
    
    job.on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
};

export default createPushNotificationsJobs;
