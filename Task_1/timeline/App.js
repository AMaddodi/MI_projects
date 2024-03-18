import logo from './logo.svg';
import './App.css';
import video1 from './videos/video1.mp4';
import video2 from './videos/video2.mp4';

function App() {
  const start_time = '00.00.00';
  const end_time = '00.10.00';
  const timestamp = ['00.00', '01.00', '02.00', '03.00','04.00', '05.00', '06.00', '07.00', '08.00', '09.00', '10.00'];

  return (
    <div style={{backgroundColor: 'black',width: '100%',height: '200px'}}>
      <div class="app-timeline">
        <div class="app-timeline-toolbar">
          <div class="app-timeline-toolbar__timings">
            <div class="app-timeline-timings">
              <div class="app-timeline-timings__current">{start_time}</div> 
              <div class="app-timeline-timings__delimiter">/</div> 
              <div class="app-timeline-timings__total">{end_time}</div>
            </div>
          </div>
        </div>
        <div class="app-timeline__trackpad">
          <div class="app-timeline-trackpad app-timeline-trackpad--sticky-supported">
            <div class="app-timeline-trackpad__sticky-box" style={{width: '956px'}}>
              <div class="app-timeline-trackpad__cursor" style={{height: '138px', transform: 'translate3d(0px, 0px, 0px)'}}>
                <div class="app-timeline-cursor">
                  <div class="app-timeline-cursor__stick"></div>
                  <div class="app-timeline-cursor__line"></div>
                </div>
                <div class="app-timeline-trackpad__cursor-alert app-timeline-trackpad__cursor-alert--align-top" style={{transform: 'translate3d(-50%, 26px, 0px)', display: 'none'}}>
                  0.00
                </div>
              </div>
              <div class="app-timeline-trackpad__ruler">
                <div class="app-timeline-ruler">
                  <div class="app-timeline-ruler__division" style={{width: '40px'}}>
                    
                      <table style={{width: '1000px', paddingleft:'50px'}}>
                        <tr>
                            {timestamp.map(stamp => (
                            <th><li>
                              <div class="app-timeline-ruler__serif app-timeline-ruler__serif--left"></div>
                              <div class="app-timeline-ruler__label app-timeline-ruler__label--left">
                              {stamp}
                              </div>
                            </li></th>
                            ))}
                        </tr>
                      </table>
                  </div>
                </div>
              </div>
            </div>
            <div class="app-timeline-trackpad__tracks" style={{width: '956px'}}>
              <div class="app-track-element-container__content">
                <div draggable="True" class="app-drag-drop-element app-drag-drop-element--drag-enabled">
                  <div class="app-drag-drop-element__source">
                    <div class="app-track-element">
                      <video width="956px" height="240" controls>
                        <source src={video1} type="video/mp4" />
                        <source src={video2} type="video/mp4" />
                      </video>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
